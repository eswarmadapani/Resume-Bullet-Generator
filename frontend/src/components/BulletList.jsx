function BulletList({ title, items }) {
  if (!items || items.length === 0) return null;

  return (
    <div className="mb-6">
      <h3 className="font-semibold mb-2">
        {title}
      </h3>

      <ul className="list-disc pl-5 space-y-1">
        {items.map((item, index) => (
          <li key={index}>{item}</li>
        ))}
      </ul>
    </div>
  );
}

export default BulletList;
