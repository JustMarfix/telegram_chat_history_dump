from dataclasses import dataclass

@dataclass()
class Config:
    api_id: int = '<app api id>'
    api_hash: str = '<app api hash>'
    invite: str = '<ссылка инвайт в формате https://t.me/joinchat>'