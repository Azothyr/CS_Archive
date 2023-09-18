import os
import json
import hashlib
from pathlib import Path
from script_tools.components.Timer import Timer


class HashHandler:
    def __init__(self, dir_path: Path, hash_file_path: Path = None):
        self.__dir_path = dir_path
        self.__hash_file_path = self.__dir_path / ".hash" if not hash_file_path else hash_file_path

    def __compute_directory_hash(self) -> str:
        sha = hashlib.sha256()
        for root, _, files in os.walk(self.__dir_path):
            for file in sorted(files):  # Sorting ensures consistent order
                file_path = os.path.join(root, file)
                with open(file_path, 'rb') as f:
                    while True:
                        data = f.read(65536)  # read in 64k chunks
                        if not data:
                            break
                        sha.update(data)
        return sha.hexdigest()

    def __get_cached_hash(self):
        if self.__hash_file_path.exists():
            with self.__hash_file_path.open('r') as f:
                cache_data = json.load(f)
                return cache_data.get(str(self.__dir_path), None)

    def cache_directory_hash(self):
        try:
            with Timer() as timer:
                cached_data = self.__get_cached_hash()
                hash_value = self.__compute_directory_hash()
                if cached_data:
                    if hash_value != cached_data['hash']:
                        self.__update_cache(hash_value)
                        message = f"UPDATED---Data was out of date hash: {hash_value}"
                    else:
                        message = f"UP TO DATE---Using cached hash: {cached_data['hash']}"
                else:
                    self.__update_cache(hash_value)
                    message = f"UPDATED---Newly computed hash: {hash_value}"

            timer.print_duration()
            return message

        except Exception as e:
            print("Error occurred:", e)

    def __update_cache(self, hash_value):
        cache_data = {}
        if self.__hash_file_path.exists():
            with self.__hash_file_path.open('r') as f:
                cache_data = json.load(f)
        cache_data[str(self.__dir_path)] = {
            "hash": hash_value,
            "timestamp": os.path.getmtime(self.__dir_path)
        }
        with self.__hash_file_path.open('w') as f:
            json.dump(cache_data, f)


if __name__ == "__main__":
    # Example usage
    hash_handler = HashHandler(Path("path_to_directory"))
    print(hash_handler.cache_directory_hash())
