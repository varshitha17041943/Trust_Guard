import React from 'react';
import { motion } from 'framer-motion';

const ScanResult = ({ events }: { events: any[] }) => {
  const finalScore = events.find(e => e.status === 'completed')?.final_risk_score;
  const agents = events.filter(e => e.agent_name);

  return (
    <motion.div 
        initial={{opacity: 0, y: 20}}
        animate={{opacity: 1, y: 0}}
        className="grid grid-cols-1 md:grid-cols-3 gap-6"
    >
      <div className="col-span-2 space-y-4">
        <h3 className="text-xl font-bold text-white">Agent Activity Log</h3>
        {agents.map((agent, idx) => (
            <motion.div 
                key={idx}
                initial={{opacity: 0, x: -20}}
                animate={{opacity: 1, x: 0}}
                className="bg-slate-800 p-4 rounded-xl border border-slate-700 flex justify-between items-center"
            >
                <div>
                    <h4 className="font-semibold text-sky-400">{agent.agent_name}</h4>
                    <pre className="text-xs text-slate-400 mt-1">{JSON.stringify(agent.finding, null, 2)}</pre>
                </div>
                <div className={`px-3 py-1 rounded-full text-xs font-bold ${agent.risk_score > 0.5 ? 'bg-red-500/20 text-red-400' : 'bg-emerald-500/20 text-emerald-400'}`}>
                    Risk: {agent.risk_score}
                </div>
            </motion.div>
        ))}
      </div>
      <div className="col-span-1">
        <div className="bg-slate-800 p-6 rounded-xl border border-slate-700 text-center sticky top-8">
            <h3 className="text-slate-400 font-medium uppercase tracking-wider mb-6">Final Assessment</h3>
            {finalScore !== undefined ? (
                <motion.div 
                    initial={{scale: 0.5, opacity: 0}}
                    animate={{scale: 1, opacity: 1}}
                    className={`w-32 h-32 mx-auto rounded-full flex items-center justify-center border-4 ${finalScore > 0.5 ? 'border-red-500 text-red-500' : 'border-emerald-500 text-emerald-500'}`}
                >
                    <span className="text-3xl font-bold">{Math.round(finalScore * 100)}%</span>
                </motion.div>
            ) : (
                <div className="w-32 h-32 mx-auto rounded-full flex items-center justify-center border-4 border-slate-600 border-t-sky-500 animate-spin">
                </div>
            )}
            <p className="mt-6 text-sm text-slate-400">
                {finalScore !== undefined 
                    ? (finalScore > 0.5 ? 'High Risk Detected. Do not proceed.' : 'Safe to proceed.')
                    : 'Agents are currently analyzing the payload...'}
            </p>
        </div>
      </div>
    </motion.div>
  );
};

export default ScanResult;
