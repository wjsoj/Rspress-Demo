// 一个计数器demo,演示react功能
import { useState } from 'react';

export default function Demo() {
  const [count, setCount] = useState(0);

  return (
    <div>
      <h1 className="my-4 font-bold">计数器</h1>
      <div className="flex flex-row space-x-2 mb-4">
        <button onClick={() => setCount(count + 1)} className="text-sm md:text-base font-semibold text-sky-700 dark:text-sky-300">+1</button>
        <p className="text-lg px-10 rounded-2xl bg-indigo-400 md:text-base font-semibold">{count}</p>
        <button onClick={() => setCount(count - 1)} className="text-sm md:text-base font-semibold text-sky-700 dark:text-sky-300">-1</button>
      </div>
    </div>
  );
}