-- Active: 1691674992801@@127.0.0.1@3306@test_db
-- stored procedure scripts that computes the average score of a student

DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;

DELIMITER $

CREATE PROCEDURE ComputeAverageScoreForUser(IN usr_id
INT) 
BEGIN
	UPDATE users
	SET average_score = (
	        SELECT AVG(score)
	        FROM corrections
	        WHERE user_id = usr_id
	    )
	WHERE id = usr_id;
	END$ 


DELIMITER ;
