import React from 'react';
import { ProgressBar } from '../../components/ui/ProgressBar';
export const ScanWorkflow = ({ onComplete }: { onComplete: () => void }) => {
  return <div><ProgressBar progress={50} /><button onClick={onComplete}>Complete</button></div>;
};
