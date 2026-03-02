import plotly.graph_objects as go

def combined_transaction_graph(df, score_map):
    fig = go.Figure()

    for _, r in df.iterrows():
        fig.add_trace(go.Scatter(
            x=[r["SourceAccount"], r["TargetAccount"]],
            y=[0, 0],
            mode="lines+markers",
            line=dict(width=2),
            marker=dict(size=10),
            hovertext=(
                f"From: {r['SourceAccount']}<br>"
                f"To: {r['TargetAccount']}<br>"
                f"Amount: {r['Amount']}<br>"
                f"Channel: {r['Channel']}"
            ),
            hoverinfo="text"
        ))

    node_x = list(set(df["SourceAccount"]) | set(df["TargetAccount"]))
    colors = []

    for acc in node_x:
        info = score_map.get(acc, {})
        if info.get("is_mule"):
            colors.append("red")
        elif info.get("mule_score", 0) > 0.2:
            colors.append("orange")
        else:
            colors.append("green")

    fig.add_trace(go.Scatter(
        x=node_x,
        y=[0]*len(node_x),
        mode="markers",
        marker=dict(size=18, color=colors),
        hovertext=node_x,
        hoverinfo="text"
    ))

    fig.update_layout(
        title="Live Money Flow Network",
        showlegend=False,
        xaxis=dict(visible=False),
        yaxis=dict(visible=False)
    )

    return fig


def single_account_graph(df, account):
    fig = go.Figure()

    sub = df[
        (df["SourceAccount"] == account) |
        (df["TargetAccount"] == account)
    ]

    for _, r in sub.iterrows():
        fig.add_trace(go.Scatter(
            x=[r["SourceAccount"], r["TargetAccount"]],
            y=[0, 0],
            mode="lines+markers",
            marker=dict(size=12),
            hovertext=(
                f"Amount: {r['Amount']}<br>"
                f"Channel: {r['Channel']}<br>"
                f"Time: {r['Timestamp']}"
            ),
            hoverinfo="text"
        ))

    fig.update_layout(
        title=f"Account Flow View: {account}",
        xaxis=dict(visible=False),
        yaxis=dict(visible=False)
    )

    return fig