DROP TABLE IF EXISTS boardgames;
CREATE TABLE boardgames (
  gameDescription text,
  imageURL varchar(255),
  maxPlayer MEDIUMINT,
  maxPlaytime MEDIUMINT,
  minAge TINYINT,
  minPlayer TINYINT,
  minPlayer MEDIUMINT,
  gameName varchar(255),
  thumbnailURL varchar(255),
  yearPublished MEDIUMINT(4),
  gameArtist varchar(255),
  gameCategory varchar(255),
  gameDesigner varchar(255),
  gameExpansion varchar(255),
  gameFamily varchar(255),
  gameMechanic varchar(255),
  gamePublisher varchar(255)
);