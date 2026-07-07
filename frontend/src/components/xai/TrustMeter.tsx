import React from 'react';
import { motion } from 'framer-motion';

export const TrustMeter = ({ score }: { score: number }) => {
  const getColor = (s: number) => {
    if (s <= 20) return '#10B981'; // Green
    if (s <= 40) return '#F59E0B'; // Yellow
    if (s <= 60) return '#F97316'; // Orange
    if (s <= 80) return '#EF4444'; // Red
    return '#991B1B'; // Dark Red
  };

  const getLabel = (s: number) => {
    if (s <= 20) return 'Safe';
    if (s <= 40) return 'Mostly Safe';
    if (s <= 60) return 'Caution';
    if (s <= 80) return 'High Risk';
    return 'Critical Danger';
  };

  const color = getColor(score);
  const label = getLabel(score);
  const percentage = Math.min(Math.max(score, 0), 100);

  return (
    <div className="flex flex-col items-center">
      <div className="relative w-48 h-48 flex items-center justify-center">
        <svg viewBox="0 0 100 50" className="w-full h-full overflow-visible">
          <path d="M 10 50 A 40 40 0 0 1 90 50" fill="none" stroke="rgba(255,255,255,0.1)" strokeWidth="12" strokeLinecap="round" />
          <motion.path
            d="M 10 50 A 40 40 0 0 1 90 50"
            fill="none"
            stroke={color}
            strokeWidth="12"
            strokeLinecap="round"
            strokeDasharray="125.6"
            initial={{ strokeDashoffset: 125.6 }}
            animate={{ strokeDashoffset: 125.6 - (125.6 * percentage) / 100 }}
            transition={{ duration: 1.5, ease: "easeOut" }}
          />
        </svg>
        <div className="absolute bottom-4 flex flex-col items-center">
          <span className="text-4xl font-black" style={{ color }}>{score}</span>
          <span className="text-xs uppercase tracking-widest text-text-muted font-bold mt-1">{label}</span>
        </div>
      </div>
    </div>
  );
};
