import React from 'react';
import { Page, AppState } from '../App';

interface Props {
  navigateTo: (page: Page) => void;
  appState: AppState;
}

export default function SkillsPage({ appState }: Props) {
  return (
    <div className="p-6">
      <h2 className="text-2xl font-bold mb-4">Recommended Skills</h2>

      <ul className="list-disc pl-6">
        <li>HTML, CSS, JavaScript</li>
        <li>React & TypeScript</li>
        <li>Problem Solving</li>
        <li>Git & GitHub</li>
      </ul>
    </div>
  );
}
