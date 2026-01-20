import AtsScore from "./AtsScore";
import BulletList from "./BulletList";

function Results({ data }) {
  return (
    <div className="mt-10">
      <AtsScore score={data.ats_score} />

      <BulletList
        title="Missing Keywords"
        items={data.missing_keywords}
      />

      <BulletList
        title="Improved Bullet Points"
        items={data.improved_bullets}
      />
    </div>
  );
}

export default Results;
