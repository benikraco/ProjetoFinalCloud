# resource "aws_vpc" "this" {
#     cidr_block = var.vpc_cidr
#     enable_dns_support = "true"
#     enable_dns_hostnames = "true"
#     tags = var.vpc_tags
# }

# resource "aws_subnet" "this" {
#     vpc_id = aws_vpc.this.id
#     cidr_block = var.subnet_cidr
#     tags = var.subnet_tags
#     availability_zone = var.availability_zone
# }