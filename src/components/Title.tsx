export default function Title({title,link,timestamp}: {title: string, link: string, timestamp: string}) {

  function formatDate(timestamp: string) {
    const date = new Date(parseInt(timestamp) * 1000);
    return date.toLocaleDateString('zh-CN', { year: 'numeric', month: 'long', day: 'numeric', hour: 'numeric', minute: 'numeric'});
  }

  return (
    <div>
      <h1 className="text-2xl md:text-3xl leading-relaxed mt-4 mb-2 font-bold">{title}</h1>
      <div className="flex flex-row space-x-10 mb-4">
        <a href={link} target="_blank" className="text-sm md:text-base font-semibold text-sky-700 dark:text-sky-300">原文链接</a>
        <p className="text-sm md:text-base font-semibold opacity-70">{formatDate(timestamp)}</p>
      </div>
    </div>
  );
}