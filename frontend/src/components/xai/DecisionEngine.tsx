import React from 'react';
import { Card } from '../ui/Card';
import { ShieldCheck, Lock, CreditCard, Share2, ShieldAlert } from 'lucide-react';

export const DecisionEngine = ({ score }: { score: number }) => {
  const getDecisions = (s: number) => {
    if (s <= 20) return { trust: 'Yes', login: 'Yes', payment: 'Yes', share: 'Yes', color: 'text-secondary', bg: 'bg-secondary/10', border: 'border-secondary/50' };
    if (s <= 40) return { trust: 'Mostly Safe', login: 'Be Careful', payment: 'Verify First', share: 'Be Careful', color: 'text-warning', bg: 'bg-warning/10', border: 'border-warning/50' };
    if (s <= 60) return { trust: 'Caution', login: 'Only if Necessary', payment: 'Verify Carefully', share: 'Avoid Sensitive Data', color: 'text-orange-500', bg: 'bg-orange-500/10', border: 'border-orange-500/50' };
    if (s <= 80) return { trust: 'No', login: 'No', payment: 'No', share: 'Never', color: 'text-danger', bg: 'bg-danger/10', border: 'border-danger/50' };
    return { trust: 'Dangerous', login: 'Never', payment: 'Never', share: 'Never', color: 'text-red-900', bg: 'bg-red-900/20', border: 'border-red-900/50' };
  };

  const d = getDecisions(score);
  const Icon = score <= 40 ? ShieldCheck : ShieldAlert;

  return (
    <div className="grid grid-cols-2 gap-4">
      <Card className={`p-4 border-l-4 ${d.border} ${d.bg}`}>
        <div className="flex items-center gap-2 mb-1"><Icon className={`w-4 h-4 ${d.color}`}/> <span className="text-sm font-semibold text-text-muted">Trust?</span></div>
        <p className={`font-black ${d.color}`}>{d.trust}</p>
      </Card>
      <Card className={`p-4 border-l-4 ${d.border} ${d.bg}`}>
        <div className="flex items-center gap-2 mb-1"><Lock className={`w-4 h-4 ${d.color}`}/> <span className="text-sm font-semibold text-text-muted">Login?</span></div>
        <p className={`font-black ${d.color}`}>{d.login}</p>
      </Card>
      <Card className={`p-4 border-l-4 ${d.border} ${d.bg}`}>
        <div className="flex items-center gap-2 mb-1"><CreditCard className={`w-4 h-4 ${d.color}`}/> <span className="text-sm font-semibold text-text-muted">Payment?</span></div>
        <p className={`font-black text-sm ${d.color}`}>{d.payment}</p>
      </Card>
      <Card className={`p-4 border-l-4 ${d.border} ${d.bg}`}>
        <div className="flex items-center gap-2 mb-1"><Share2 className={`w-4 h-4 ${d.color}`}/> <span className="text-sm font-semibold text-text-muted">Share Info?</span></div>
        <p className={`font-black text-sm ${d.color}`}>{d.share}</p>
      </Card>
    </div>
  );
};
