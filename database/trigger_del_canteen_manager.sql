CREATE TRIGGER TRIGGER_DELETE_CANTEEN_MANAGER
AFTER DELETE ON user_info
FOR EACH ROW
DELETE FROM user_info WHERE user_info.id = OLD.id
