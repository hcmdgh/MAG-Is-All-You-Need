DROP TABLE IF EXISTS MAG.field;

CREATE TABLE MAG.field (
    id BIGINT PRIMARY KEY,
    `rank` BIGINT, 
    normalized_name TEXT, 
    display_name TEXT, 
    main_type TEXT, 
    level BIGINT, 
    paper_count BIGINT, 
    paper_family_count BIGINT, 
    citation_count BIGINT, 
    created_date TEXT
);
