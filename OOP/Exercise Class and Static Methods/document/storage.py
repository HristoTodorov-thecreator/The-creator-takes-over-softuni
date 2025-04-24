from document.category import Category
from document.topic import Topic
from document.document import Document

class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []


    def add_category(self,category: Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self,topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self,document: Document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self,category_id: int, new_name: str):
        for category in self.categories:
            if category.id == category_id:
                category.edit(new_name)
                break

    def edit_topic(self,topic_id: int, new_topic: str, new_storage_folder: str):
        for topic in self.topics:
            if topic.id == topic_id:
                topic.edit(new_topic,new_storage_folder)
                break

    def edit_document(self,document_id: int, new_file_name: str):
        for document in self.documents:
            if document.id == document_id:
                document.edit(new_file_name)
                break

    def delete_category(self,category_id):
        self.categories = [c for c in self.categories if c.id != category_id]

    def delete_topic(self, topic_id: int):
        self.topics = [t for t in self.topics if t.id != topic_id]

    def delete_document(self, document_id: int):
        self.documents = [d for d in self.documents if d.id != document_id]

    def get_document(self, document_id: int):
        for document in self.documents:
            if document.id == document_id:
                return document

    def __repr__(self):
        return '\n'.join([repr(doc) for doc in self.documents])

