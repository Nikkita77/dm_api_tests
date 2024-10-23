from pydantic import (
    BaseModel,
    Field,
    ConfigDict,
)


class LoginCredentials(BaseModel):
    model_config = ConfigDict(extra="forbid")  # Все поля модели обязательны к заполнению
    login: str = Field(..., description="Логин")
    password: str = Field(..., description="Пароль")
    remember_me: bool = Field(..., description="Запомнить меня", alias="rememberMe")
