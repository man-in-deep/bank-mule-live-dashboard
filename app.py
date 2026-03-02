import streamlit as st
import pandas as pd

from core.ingestion import load_transactions
from core.csv_generator import start_periodic_generation
from core.database import init_db
from core.scenarios import run_all_scenarios
from core.scoring import compute_mule_scores
from core.graphs import combined_transaction_graph, single_account_graph
from core.alert_history import save_alert, load_alerts
from core.sar_export import export_sar_csv, export_sar_pdf
from core.llm import explain_mule

st.set_page_config(layout="wide")

with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("🏦 Bank Mule Detection – Live Dashboard")

init_db()
start_periodic_generation()

df = load_transactions()

scenario_map = run_all_scenarios(df)
scores = compute_mule_scores(scenario_map)

for acc, info in scores.items():
    if info["is_mule"]:
        save_alert(acc, info["mule_score"], info["scenarios"])

st.subheader("Live Money Flow")
st.plotly_chart(
    combined_transaction_graph(df, scores),
    use_container_width=True
)

account = st.selectbox("Drill Down Account", sorted(scores.keys()))

if account:
    st.plotly_chart(
        single_account_graph(df, account),
        use_container_width=True
    )

    st.subheader("Mule Analysis")
    st.json(scores[account])

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("Export SAR CSV"):
            export_sar_csv(account, scores[account], "sar.csv")
            st.success("CSV exported")

    with col2:
        if st.button("Export SAR PDF"):
            export_sar_pdf(account, scores[account], "sar.pdf")
            st.success("PDF exported")

    with col3:
        if st.button("LLM Recommendation"):
            st.write(explain_mule(account, scores[account]))

st.subheader("Alert History")
st.table(load_alerts())