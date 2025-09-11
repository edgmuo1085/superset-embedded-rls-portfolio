import os
import logging
from datetime import timedelta

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info("⚡ Config personalizada cargada ⚡")


### IMPRIMIR VARIABLES DE ENTORNO   
logger.info("ALLOWED_EMBEDDED_DOMAINS: %s", os.environ.get("ALLOWED_EMBEDDED_DOMAINS", "http://localhost:3001"))
logger.info("SUPERSET_SECRET_KEY: %s", os.environ.get("SUPERSET_SECRET_KEY", "a-very-secure-secret-key"))
logger.info("SUPERSET_JWT_SECRET: %s", os.environ.get("SUPERSET_JWT_SECRET", "a-very-secure-secret-key"))
logger.info("SUPERSET_SQLALCHEMY_DATABASE_URI: %s", os.environ.get("SUPERSET_SQLALCHEMY_DATABASE_URI", "postgresql+psycopg2://superset:superset@db:5432/superset"))


# ==============================
# 🔑 Claves seguras desde variables de entorno
# ==============================
SECRET_KEY = os.getenv("SUPERSET_SECRET_KEY", "default_inseguro_cambiar")
JWT_SECRET = os.getenv("SUPERSET_JWT_SECRET", "jwt_inseguro_cambiar")

# --- Settings for Embedding & Guest Tokens ---
# ENABLE_EMBEDDED_SUPERSET is controlled by env var

ALLOWED_EMBEDDED_DOMAINS = os.environ.get("ALLOWED_EMBEDDED_DOMAINS", "").split(",")
ALLOWED_EMBEDDED_DOMAINS = [domain.strip() for domain in ALLOWED_EMBEDDED_DOMAINS if domain.strip()]
if not ALLOWED_EMBEDDED_DOMAINS:
    ALLOWED_EMBEDDED_DOMAINS = ["http://localhost:3001"]

# ==============================
# 🖼️ Embedding en iframes
# ==============================
ALLOW_IFRAME_EMBED = True
HTTP_HEADERS = {
    "X-Frame-Options": "ALLOWALL"
}
TALISMAN_ENABLED = False

# ==============================
# 🚀 Feature flags
# ==============================
FEATURE_FLAGS = {
    "EMBEDDED_SUPERSET": True,
    "EMBEDDED_SUPERSET_DYNAMIC_PLUGINS": True,
    "DASHBOARD_NATIVE_FILTERS": True,
    "DASHBOARD_CROSS_FILTERS": True,
    "ENABLE_TEMPLATE_PROCESSING": True,
}

# ==============================
# 👤 Configuración del rol invitado
# ==============================
GUEST_ROLE_NAME = "Gamma"

# ==============================
# 🔑 Configuración de JWT (para SDK)
# ==============================
EMBEDDED_SUPERSET = {
    "guest_token_jwt_secret": JWT_SECRET,
    "guest_token_jwt_exp_seconds": int(timedelta(hours=1).total_seconds()),
    "allowed_domains": ALLOWED_EMBEDDED_DOMAINS,
}

logger.info("✅ Embedding habilitado con rol %s", GUEST_ROLE_NAME)
