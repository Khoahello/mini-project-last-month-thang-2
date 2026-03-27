# Bài tập API Quản lý Sản phẩm

Dự án Backend xây dựng API cơ bản sử dụng Flask, Blueprint và lưu trữ dữ liệu
bằng file JSON.

## Cách chạy dự án

1. Kích hoạt môi trường và cài đặt thư viện: `pip install Flask`
2. Chạy ứng dụng: `python app.py`

## Danh sách API (Test qua Postman)

- **GET** `/products` : Xem danh sách sản phẩm (Tìm kiếm: `/products?name=xyz`)
- **GET** `/product/<id>` : Xem chi tiết 1 sản phẩm
- **POST** `/products` : Thêm sản phẩm (ID tự động tăng)
- **PUT** `/product/<id>` : Cập nhật thông tin sản phẩm
- **DELETE** `/product/<id>` : Xóa sản phẩm
