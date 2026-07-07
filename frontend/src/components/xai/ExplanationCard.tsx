import React from 'react';
import { Card } from '../ui/Card';
import { AlertTriangle, Info } from 'lucide-react';

interface Props {
  title: string;
  severity: string;
  explanation: string;
}

export const ExplanationCard = ({ title, severity, explanation }: Props) => {
  const isHigh = severity === 'High' || severity === 'Critical';
  const color = isHigh ? 'text-danger' : 'text-warning';
  
  return (
    <Card className="flex flex-col h-full border-white/5 hover:border-white/20 transition-colors">
      <div className="flex items-center gap-2 mb-3">
        <AlertTriangle className={`w-5 h-5 ${color}`} />
        <h4 className="font-bold">{title}</h4>
      </div>
      <span className={`text-xs font-bold uppercase tracking-wider mb-2 ${color}`}>{severity} Risk</span>
      <p className="text-sm text-text-muted flex-grow mb-4">{explanation}</p>
      <div className="mt-auto pt-4 border-t border-white/5">
        <p className="text-xs text-primary flex items-center gap-1 font-medium cursor-pointer hover:underline">
          <Info className="w-3 h-3" /> Learn why this matters
        </p>
      </div>
    </Card>
  );
};
