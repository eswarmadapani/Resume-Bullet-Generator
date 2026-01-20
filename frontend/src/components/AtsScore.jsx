function AtsScore({ score }) {
  return (
    <div className="text-center mb-8">
      <h2 className="text-xl font-semibold">
        ATS Score
      </h2>
      <p className="text-5xl font-bold mt-2">
        {score}
      </p>
    </div>
  );
}

export default AtsScore;
