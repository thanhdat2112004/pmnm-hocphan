Nghiên cứu sự kiện HashiCorp chuyển Terraform sang BUSL-1.1 và sự ra đời của OpenTofu (880 từ)
1. Bối cảnh lịch sử và vai trò của Terraform
Terraform, được ra mắt bởi HashiCorp vào năm 2014, là công cụ Quản lý Hạ tầng dưới dạng Mã nguồn (Infrastructure as Code - IaC) phổ biến nhất thế giới. Trong gần một thập kỷ, Terraform được phát hành dưới giấy phép Mozilla Public License 2.0 (MPL-2.0) — một giấy phép mã nguồn mở thân thiện, thuộc nhóm copyleft yếu, cho phép cá nhân và tổ chức tự do tích hợp, sửa đổi và xây dựng các giải pháp xung quanh hệ sinh thái Terraform. Sự cởi mở này đã giúp Terraform trở thành tiêu chuẩn thực tế (de facto standard) trong quản trị hạ tầng đám mây, xây dựng nên một cộng đồng đóng góp khổng lồ gồm các nhà phát triển, nhà cung cấp dịch vụ đám mây (AWS, Azure, GCP) và vô số công ty khởi nghiệp.

2. Bước ngoặt lịch sử: Chuyển đổi sang BUSL-1.1 năm 2023
Vào ngày 10 tháng 8 năm 2023, HashiCorp bất ngờ thông báo thay đổi giấy phép của toàn bộ các sản phẩm cốt lõi (bao gồm Terraform, Vault, Consul, Nomad) từ MPL-2.0 sang Business Source License 1.1 (BUSL-1.1), bắt đầu từ phiên bản Terraform 1.6.

Bản chất của giấy phép BUSL-1.1: BUSL không phải là một giấy phép mã nguồn mở được công nhận bởi Open Source Initiative (OSI). Mặc dù mã nguồn vẫn công khai để xem, sao chép và sửa đổi, BUSL đặt ra hạn chế thương mại quan trọng: Cấm việc sử dụng phần mềm để cung cấp các sản phẩm/dịch vụ cạnh tranh trực tiếp với thương phẩm thương mại của HashiCorp.

Điều khoản Chuyển đổi (Change License Date): BUSL-1.1 quy định sau một thời gian nhất định (thường là 4 năm), mã nguồn của phiên bản đó sẽ tự động chuyển về lại giấy phép mã nguồn mở truyền thống (như Apache 2.0 hoặc MPL-2.0).

Lý do từ HashiCorp: HashiCorp cho rằng nhiều vendors/công ty thương mại đã lợi dụng mã nguồn mở miễn phí của Terraform để xây dựng các nền tảng thương mại cạnh tranh trực tiếp với các sản phẩm trả phí của HashiCorp (như Terraform Cloud/Enterprise) mà không đóng góp lại tương xứng cho cộng đồng hoặc chi trả chi phí R&D.

3. Làn sóng phản đối và sự ra đời của OpenTofu
Quyết định đơn phương của HashiCorp đã gây ra làn sóng chấn động và bất bình sâu sắc trong cộng đồng DevOps và các doanh nghiệp. Nhóm chịu ảnh hưởng nặng nề nhất là các công ty phát triển công cụ dựa trên Terraform như Spacelift, env0, Scalr hay Harness.

Chỉ vài tuần sau thông báo của HashiCorp, vào ngày 25 tháng 8 năm 2023, một liên minh gồm nhiều công ty công nghệ và các nhà đóng góp mã nguồn độc lập đã thành lập OpenTF Initiative. Mục tiêu của họ là duy trì một bản fork thực sự tự do, mã nguồn mở, độc lập và tuân thủ các nguyên tắc của OSI dựa trên phiên bản Terraform 1.5.6 (phiên bản cuối cùng dùng giấy phép MPL-2.0).

Đến tháng 9 năm 2023, dự án chính thức đổi tên thành OpenTofu và được nộp gia nhập Linux Foundation — tổ chức phi lợi nhuận uy tín hàng đầu về quản trị phần mềm mã nguồn mở. Điều này đảm bảo rằng OpenTofu sẽ thuộc sở hữu của cộng đồng chứ không nằm dưới sự chi phối thương mại của bất kỳ công ty đơn lẻ nào.
Tiêu chí	Terraform (HashiCorp)	OpenTofu (Linux Foundation)			
Giấy phép	BUSL 1.1 (Source-available, cấm cạnh tranh)	MIT License (Mã nguồn mở chuẩn OSI)			
Mô hình quản trị	Doanh nghiệp kiểm soát (Vendor-driven)	Cộng đồng trung lập (Linux Foundation)			
Khả năng tương thích	Tương thích ngược với các phiên bản cũ	Tương thích hoàn toàn 1:1 với Terraform <=1.5.x			
Tính năng mới	Tập trung vào tính năng cao cấp cho Enterprise	Bổ sung các tính năng cộng đồng yêu cầu (ví dụ: State Encryption)			
5. Tác động và Ý nghĩa đối với Ngành Công nghệ
Sự kiện HashiCorp chuyển sang BUSL và sự ra đời của OpenTofu để lại những bài học sâu sắc cho toàn bộ ngành công nghiệp phần mềm:

Khái niệm "Source-Available" vs. "Open Source": Việc các công ty công nghệ lớn (Elastic, MongoDB, Redis, HashiCorp) liên tục chuyển đổi sang các giấy phép thương mại như SSPL hay BUSL làm mờ ranh giới giữa mã nguồn mở thực sự và mã nguồn "chỉ được xem". Điều này buộc các kiến trúc sư phần mềm phải thẩm định kỹ lưỡng yếu tố pháp lý trước khi đưa một công nghệ vào hạ tầng cốt lõi.

Rủi ro phụ thuộc vào một Vendor (Vendor Lock-in): Khi một dự án mã nguồn mở do duy nhất một công ty thương mại kiểm soát sở hữu bản quyền, cộng đồng luôn đối mặt với rủi ro bị thay đổi luật chơi bất kỳ lúc nào.

Sức mạnh của Cộng đồng và các Tổ chức Trung lập: Sự thành công nhanh chóng của OpenTofu dưới trướng Linux Foundation chứng minh rằng nếu cộng đồng đủ lớn và đoàn kết, họ hoàn toàn có khả năng "giải cứu" công nghệ và duy trì giá trị cốt lõi của phần mềm tự do nguồn mở.
