import React from 'react';
import { Page, AppState } from '../App';

interface Props {
  navigateTo: (page: Page) => void;
  appState: AppState;
}

export default function InterviewPrepPage({ navigateTo, appState }: Props) {
  return (
    <div className="p-6">
      <h2 className="text-2xl font-bold mb-4">Interview Preparation</h2>

      <ul className="list-disc pl-6">
        <li>HR Questions</li>
        <li>Technical Questions</li>
        <li>Mock Interviews</li>
      </ul>
    </div>
  );
}
