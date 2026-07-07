import React from 'react';
import { motion } from 'framer-motion';

export const RiskBreakdown = () => {
  // Mock breakdown data per prompt request
  const breakdown = [
    { label: 'Threat Intelligence', value: 35, color: 'bg-danger' },
    { label: 'Brand Similarity', value: 25, color: 'bg-orange-500' },
    { label: 'SSL Certificate', value: 15, color: 'bg-warning' },
    { label: 'WHOIS / Domain Age', value: 15, color: 'bg-secondary' },
    { label: 'URL Pattern', value: 10, color: 'bg-primary' },
  ];

  return (
    <div className="space-y-4">
      <h3 className="font-semibold text-sm uppercase tracking-widest text-text-muted mb-4">Risk Score Breakdown</h3>
      {breakdown.map((item, idx) => (
        <div key={idx} className="space-y-1">
          <div className="flex justify-between text-xs font-medium">
            <span>{item.label}</span>
            <span>{item.value}%</span>
          </div>
          <div className="w-full bg-white/5 h-2 rounded-full overflow-hidden">
            <motion.div 
              initial={{ width: 0 }}
              animate={{ width: `${item.value}%` }}
              transition={{ duration: 1, delay: idx * 0.2 }}
              className={`h-full ${item.color}`}
            />
          </div>
        </div>
      ))}
    </div>
  );
};
