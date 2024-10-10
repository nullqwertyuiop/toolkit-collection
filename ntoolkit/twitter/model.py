from dataclasses import dataclass
from datetime import datetime
from typing import Literal, Self


@dataclass
class TweetUserStatistics:
    followers_count: int
    friends_count: int
    listed_count: int
    favourites_count: int
    statuses_count: int


@dataclass
class TweetUserStatus:
    followed_by: bool | None
    following: bool | None
    can_dm: bool | None


@dataclass
class TweetUser:
    id: int
    name: str
    screen_name: str
    location: str
    description: str
    protected: bool
    verified: bool
    created_at: datetime
    statistics: TweetUserStatistics
    status: TweetUserStatus
    pinned_tweet_ids: list[int]
    profile_image: str
    profile_banner: str | None

    @property
    def handle(self):
        return f"@{self.screen_name}"


@dataclass
class TweetStatistics:
    views_count: int
    bookmark_count: int
    favourite_count: int
    quote_count: int
    reply_count: int
    retweet_count: int


@dataclass
class TweetStatus:
    bookmarked: bool
    favourited: bool  # noqa
    retweeted: bool


@dataclass
class TweetEntityHashTag:
    indices: list[int]
    text: str


@dataclass
class TweetEntityMedia:
    type: Literal["photo", "video", "animated_gif"]
    indices: list[int]
    url: str
    expanded_url: str


@dataclass
class TweetEntitySymbol:
    indices: list[int]
    text: str


@dataclass
class TweetEntityTimestamp:
    indices: list[int]


@dataclass
class TweetEntityUrl:
    indices: list[int]
    display_url: str
    expanded_url: str
    url: str


@dataclass
class TweetEntityUserMention:
    id: int
    name: str
    screen_name: str
    indices: list[int]


@dataclass
class TweetEntities:
    hashtags: list[TweetEntityHashTag]
    media: list[TweetEntityMedia]
    symbols: list[TweetEntitySymbol]
    timestamps: list[TweetEntityTimestamp]
    urls: list[TweetEntityUrl]
    user_mentions: list[TweetEntityUserMention]


@dataclass
class Tweet:
    id: int
    created_at: datetime
    full_text: str
    display_text_range: list[int]
    lang: str
    possibly_sensitive: bool | None
    statistics: TweetStatistics
    status: TweetStatus
    entities: TweetEntities
    conversation_threads: list[Self]
    user: TweetUser

    @property
    def text(self) -> str:
        return self.full_text[self.display_text_range[0] : self.display_text_range[1]]
