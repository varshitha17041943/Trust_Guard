import React from 'react';
import { cn } from '../../utils/cn';

export const RiskBadge = ({ level, className }: { level: string, className?: string }) => {
  const styles: Record<string, string> = {
    'Safe': 'bg-secondary/20 text-secondary border-secondary/30',
    'Low': 'bg-yellow-500/20 text-yellow-500 border-yellow-500/30',
    'Medium': 'bg-orange-500/20 text-orange-500 border-orange-500/30',
    'High': 'bg-danger/20 text-danger border-danger/30',
    'Critical': 'bg-red-900/40 text-red-400 border-red-900/50',
  };
  return (
    <span className={cn('inline-flex items-center rounded-full border px-2.5 py-0.5 text-xs font-semibold', styles[level] || styles['Safe'], className)}>
      {level}
    </span>
  );
};
