import React from 'react';
import { Card } from '../ui/Card';
import { ShieldCheck, ExternalLink, ShieldAlert } from 'lucide-react';

export const OfficialWebsite = ({ officialData }: { officialData?: any }) => {
  const hasOfficial = officialData && officialData.url && officialData.url !== 'N/A';

  if (!hasOfficial) {
    return (
      <Card className="bg-background-paper border-white/10 p-4 flex items-center gap-3">
        <ShieldAlert className="w-6 h-6 text-text-muted" />
        <p className="text-sm text-text-muted">No verified official website could be identified for this domain.</p>
      </Card>
    );
  }

  return (
    <Card className="bg-primary/10 border-primary/30 relative overflow-hidden p-6">
      <div className="absolute top-0 left-0 w-1 h-full bg-primary"></div>
      <div className="flex items-start gap-4">
        <div className="bg-primary/20 p-3 rounded-full shrink-0">
          <ShieldCheck className="w-6 h-6 text-primary" />
        </div>
        <div>
          <h3 className="font-bold text-lg mb-1 flex items-center gap-2">Verified Official Website</h3>
          <p className="text-text-muted text-sm mb-4">We detected this scan might be attempting to impersonate a known brand. Please use the official verified link below.</p>
          <a href={officialData.url} target="_blank" rel="noreferrer" className="inline-flex items-center px-4 py-2 bg-primary text-white rounded-lg hover:bg-primary-light font-medium transition-colors text-sm">
            Visit {officialData.url}
            <ExternalLink className="w-4 h-4 ml-2" />
          </a>
          <p className="text-xs text-primary/70 mt-3 font-mono">Verification Confidence: {officialData.confidence}%</p>
        </div>
      </div>
    </Card>
  );
};
