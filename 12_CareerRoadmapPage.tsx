import React from 'react';
import { Page, AppState } from '../App';

interface Props {
  navigateTo: (page: Page) => void;
  appState: AppState;
}

export default function CareerRoadmapPage({ navigateTo, appState }: Props) {
  return (
    <div className="p-6">
      <h2 className="text-2xl font-bold mb-4">Career Roadmap</h2>

      <ol className="list-decimal pl-6">
        <li>Learn fundamentals</li>
        <li>Build projects</li>
        <li>Do internships</li>
        <li>Apply for jobs</li>
      </ol>
    </div>
  );
}
