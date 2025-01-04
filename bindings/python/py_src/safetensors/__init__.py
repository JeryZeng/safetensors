# Re-export this
from ._safetensors_rust import (  # noqa: F401
    SafetensorError,
    __version__,
    deserialize,
    deserialize_file_concurrently,
    safe_open,
    serialize,
    serialize_file,
)
