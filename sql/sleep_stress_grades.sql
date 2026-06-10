-- sleep_stress_grades.sql
-- Effect of sleep quality and stress on academic performance.

-- 1. Sleep quality vs grades
SELECT
    sleep_quality,
    COUNT(*)                                AS student_count,
    ROUND(AVG(grades), 2)                   AS avg_grades,
    ROUND(AVG(gaming_hours), 2)             AS avg_gaming_hours,
    ROUND(AVG(study_hours), 2)              AS avg_study_hours,
    ROUND(AVG(reaction_time_ms), 1)         AS avg_reaction_ms,
    ROUND(AVG(stress_encoded), 2)           AS avg_stress_score
FROM gaming_students
GROUP BY sleep_quality
ORDER BY sleep_quality;

-- 2. Stress × sleep × grades matrix
SELECT
    stress_level,
    sleep_quality,
    COUNT(*)                                AS student_count,
    ROUND(AVG(grades), 2)                   AS avg_grades,
    ROUND(AVG(gaming_hours), 2)             AS avg_gaming_hours
FROM gaming_students
GROUP BY stress_level, sleep_quality
ORDER BY
    CASE stress_level WHEN 'Low' THEN 1 WHEN 'Medium' THEN 2 ELSE 3 END,
    sleep_quality;

-- 3. Students with poor sleep AND high addiction — at-risk cohort
SELECT
    COUNT(*)                                AS at_risk_count,
    ROUND(AVG(grades), 2)                   AS avg_grades,
    ROUND(AVG(gaming_hours), 2)             AS avg_gaming_hours,
    ROUND(AVG(attendance), 2)               AS avg_attendance
FROM gaming_students
WHERE sleep_quality = 'Poor (<5h)'
  AND addiction_level IN ('High', 'Severe');
