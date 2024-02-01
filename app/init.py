import json
from app.api.ImageApiTranslator import ImageApiTranslator
from app.getter.ImageGetter import ImageGetter


class Init:
	def __init__(self):
		self.translator = ImageApiTranslator()
		self.getter = ImageGetter()
		self.space = None
		self.protocol = None
		self.base_type = None
		self.subtype = None
		self.request_type = None

	def run(self, request: str):
		"""
		Точка входа в приложение.
		:param request: Request (in progress)
		:return: Response (in progress)
		"""
		match request:
			case "get":
				return self.getter.run()

		# self.__parse_meta(meta)
		# request_dict = self.translator.match_type(self.protocol)
		# self.translator.set_operation = self.request_type
		# self.translator.match_api()
		# if self.translator.comparsion_request(request_dict.get(self.request_type)):
		# 	response_json = self.getter.run()
		# if self.translator.comparsion_response(response_json):
		# 	return self.success(response_json)
		# return self.error()

	def __parse_meta(self, meta: str) -> None:
		"""
		meta - идентификатор запроса.
		Состоит из пространства, формата передачи, сервиса, подсервиса (если есть) и операции.
		Пример: universe.json.file.image.get
		:param meta: str
		:return: None
		"""
		meta_types = meta.split('.')
		self.space = meta_types[0]
		self.protocol = meta_types[1]
		self.base_type = meta_types[2]
		match len(meta_types):
			case 4:
				pass
			case 5:
				self.subtype = meta_types[3]
				self.request_type = "GetOne" if meta_types[4] == 'get' else ""
			case _:
				print("request meta error: also two meta args needed")

	def success(self, response_json):
		self.translator.response['Success'] = response_json

	def error(self):
		self.translator.response['Error'] = 0
		