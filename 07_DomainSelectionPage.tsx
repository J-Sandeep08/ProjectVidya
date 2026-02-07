import React, { useState } from 'react';
import { Page, AppState } from '../App';

interface Props {
  navigateTo: (page: Page) => void;
  appState: AppState;
  updateAppState: (updates: Partial<AppState>) => void;
}

const domains = [
  'Web Development',
  'Data Science',
  'AI / ML',
  'Cyber Security',
  'Cloud Computing',
  'Mobile App Development',
];

export default function DomainSelectionPage({ navigateTo, updateAppState }: Props) {
  const [selected, setSelected] = useState<string | null>(null);

  const handleNext = () => {
    if (!selected) return;
    updateAppState({
      selectedDomain: selected,
      completedSteps: { resume: true, eligibility: true, domain: true },
    });
    navigateTo('dashboard');
  };

  return (
    <div className="p-6">
      <h2 className="text-2xl font-bold mb-4">Select Your Career Domain</h2>

      <div className="grid grid-cols-2 gap-4">
        {domains.map(domain => (
          <button
            key={domain}
            onClick={() => setSelected(domain)}
            className={`p-4 border rounded ${
              selected === domain ? 'bg-blue-500 text-white' : 'bg-white'
            }`}
          >
            {domain}
          </button>
        ))}
      </div>

      <button
        onClick={handleNext}
        className="mt-6 px-6 py-2 bg-green-600 text-white rounded"
      >
        Confirm Domain
      </button>
    </div>
  );
}
