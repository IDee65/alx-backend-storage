-- Active: 1691674992801@@127.0.0.1@3306@test_db

-- list all bands with Glam rock as their main style, sorted by the number

-- of fans they have (in descending order)

SELECT
    band_name,
    IFNULL(split, 2022) - formed AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;
