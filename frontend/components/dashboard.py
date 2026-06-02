import streamlit as st
import pandas as pd
import plotly.express as px

def render_dashboard():

    if st.session_state.performance_history:

        st.divider()

        st.header(
            "📈 Learning Progress Dashboard"
        )

        df = pd.DataFrame(
            st.session_state.performance_history
        )

        df["Attempt"] = range(
            1,
            len(df) + 1
        )

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "🏆 Best Score",
                f"{max(df['score'])}%"
            )

        with col2:

            st.metric(
                "📊 Average Score",
                f"{round(df['score'].mean(), 2)}%"
            )

        fig = px.line(
            df,
            x="Attempt",
            y="score",
            markers=True,
            title="📈 Learning Progress Over Time"
        )

        fig.update_traces(
            line_width=4,
            marker_size=10
        )

        fig.update_layout(
            xaxis_title="Quiz Attempt",
            yaxis_title="Score (%)",
            hovermode="x unified",
            template="plotly_white"
        )

        fig.add_hline(
            y=80,
            line_dash="dash",
            annotation_text="Excellent"
        )

        fig.add_hline(
            y=60,
            line_dash="dash",
            annotation_text="Good"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        st.subheader(
            "📋 Performance History"
        )

        for idx, attempt in enumerate(
            st.session_state.performance_history,
            start=1
        ):

            st.write(
                f"Attempt {idx} | "
                f"Topic: {attempt['topic']} | "
                f"Score: {attempt['score']}%"
            )
        
# =====================================================
# 💼 RESUME INTERVIEW ANALYTICS
# =====================================================

    if st.session_state.resume_history:

        st.divider()

        st.header(
            "💼 Resume Interview Analytics"
        )

        resume_df = pd.DataFrame(
            st.session_state.resume_history
        )

        col1, col2, col3 = st.columns(3)

        with col1:

            st.metric(
                "🏆 Best Resume Score",
                f"{resume_df['score'].max()}/10"
            )

        with col2:

            st.metric(
                "📊 Average Resume Score",
                f"{round(resume_df['score'].mean(), 2)}/10"
            )

        with col3:

            st.metric(
                "🎯 Interview Attempts",
                len(resume_df)
            )

        fig = px.line(
            resume_df,
            x="round",
            y="score",
            markers=True,
            title=
            "📈 Resume Interview Progress"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )
        st.subheader(
            "📋 Resume Interview History"
        )

        for attempt in st.session_state.resume_history:

            st.success(
                f"Round {attempt['round']} | "
                f"Score: {attempt['score']}/10"
            )