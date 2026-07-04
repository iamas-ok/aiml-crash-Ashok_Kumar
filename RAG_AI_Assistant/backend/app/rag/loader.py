from pathlib import Path


class DocumentLoader:

    def __init__(self, folder_path: str):
        self.folder_path = Path(folder_path)

    def load_documents(self):

        documents = []

        txt_files = sorted(self.folder_path.glob("*.txt"))

        for file in txt_files:

            text = file.read_text(
                encoding="utf-8"
            )

            documents.append(
                {
                    "file_name": file.name,
                    "content": text
                }
            )

        return documents