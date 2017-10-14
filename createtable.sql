DROP TABLE IF EXISTS boardgames;
CREATE TABLE boardgames (
  gameDescription text,
  imageURL varchar(255),
  maxPlayer smallint,
  maxPlaytime int,
  minAge smallint,
  minPlayer smallint,
  minPlaytime int,
  gameName varchar(255),
  thumbnailURL varchar(255),
  yearPublished smallint,
  gameArtist text,
  gameCategory text,
  gameDesigner text,
  gameExpansion text,
  gameFamily text,
  gameMechanic text,
  gamePublisher text
);