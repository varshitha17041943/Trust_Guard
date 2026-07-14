import sys
import os
import asyncio
import streamlit as st

# Add the 'backend' directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'backend')))

from app.agents.core.state import SharedContext
from app.services.scan_service import orchestrator

# Streamlit Page Configuration
st.set_page_config(
    page_title="TrustGuardAI Multi-Agent Scanner",
    page_icon="🛡️",
    layout="centered"
)

st.title("🛡️ TrustGuardAI Multi-Agent Scanner")
st.markdown("### Autonomous AI Threat Detection for Kaggle")
st.markdown("Enter a URL below. Our **ADK Multi-Agent DAG Orchestrator** will deploy multiple AI agents in the background to analyze the target for phishing, brand impersonation, and security risks.")

# Input
target_url = st.text_input("Target URL to Scan", placeholder="https://example.com")

if st.button("Run Multi-Agent Scan", type="primary"):
    if not target_url:
        st.warning("Please enter a URL to scan.")
    else:
        st.info("🚀 Initializing Multi-Agent DAG Orchestrator...")
        
        # Create an async wrapper to run the orchestrator
        async def run_scan():
            context = SharedContext(original_target=target_url, scan_type="URL")
            
            with st.spinner("Agents are analyzing the target... (This may take 10-15 seconds)"):
                final_state = await orchestrator.run(context)
                return final_state
                
        # Run the async function synchronously in Streamlit
        try:
            result_state = asyncio.run(run_scan())
            
            st.success("✅ Multi-Agent Scan Complete!")
            
            # Display Results
            col1, col2 = st.columns(2)
            with col1:
                st.metric(label="Risk Score", value=f"{result_state.risk_score}/100")
            with col2:
                st.metric(label="Risk Level", value=result_state.risk_level)
                
            st.markdown("---")
            
            st.subheader("🚩 Threat Intelligence Flags")
            if result_state.threat_intel_flags:
                for flag in result_state.threat_intel_flags:
                    st.error(f"- {flag}")
            else:
                st.success("No active threats detected by the ThreatIntelAgent.")
                
            st.markdown("---")
            
            st.subheader("💡 Recommendations")
            if result_state.recommendations:
                for rec in result_state.recommendations:
                    st.info(f"- {rec}")
            else:
                st.write("No recommendations.")
                
        except Exception as e:
            st.error(f"An error occurred during the agent execution: {e}")
