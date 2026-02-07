import React from 'react';
import { Page, AppState } from '../App';

interface Props {
  navigateTo: (page: Page) => void;
  appState: AppState;
}

export default function JobListingsPage({ navigateTo, appState }: Props) {
  return (
    <div className="p-6">
      <h2 className="text-2xl font-bold mb-4">Job Listings</h2>

      <p className="mb-4">
        Showing jobs for: <b>{appState.selectedDomain ?? 'All Domains'}</b>
      </p>

      <ul className="space-y-3">
        <li className="border p-3 rounded">
          Frontend Developer Intern – Company A
        </li>
        <li className="border p-3 rounded">
          Junior Software Engineer – Company B
        </li>
        <li className="border p-3 rounded">
          Trainee Developer – Company C
        </li>
      </ul>

      <button
        onClick={() => navigateTo('skills')}
        className="mt-6 px-6 py-2 bg-blue-600 text-white rounded"
      >
        View Required Skills →
      </button>
    </div>
  );
}
