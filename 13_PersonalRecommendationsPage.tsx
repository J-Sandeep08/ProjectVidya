import React from 'react';
import { Page, AppState } from '../App';

interface Props {
  navigateTo: (page: Page) => void;
  appState: AppState;
}

export default function PersonalRecommendationsPage({ appState }: Props) {
  return (
    <div className="p-6">
      <h2 className="text-2xl font-bold mb-4">Personalized Recommendations</h2>

      <p>
        Based on your interest in <b>{appState.selectedDomain}</b>, we recommend:
      </p>

      <ul className="list-disc pl-6 mt-3">
        <li>Build 2 real-world projects</li>
        <li>Apply for internships</li>
        <li>Improve problem-solving skills</li>
      </ul>
    </div>
  );
}
