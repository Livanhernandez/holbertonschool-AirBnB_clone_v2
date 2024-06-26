-- script that creates tables in database
CREATE TABLE states (
  id VARCHAR(60) NOT NULL,
  created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  name VARCHAR(128) NOT NULL,
  PRIMARY KEY(id)
  );

CREATE TABLE cities (
  id VARCHAR(60) NOT NULL,
  created_at datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  state_id VARCHAR(60) NOT NULL,
  PRIMARY KEY (id),
  KEY state_id (state_id),
  CONSTRAINT fk_state_id FOREIGN KEY (state_id) REFERENCES states (id)
  );