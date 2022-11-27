resource "aws_internet_gateway" "my-gateway" {
    vpc_id = aws_vpc.this.id
    tags = var.gateway_tags
}

resource "aws_route_table" "my-route-table" {
    vpc_id = aws_vpc.this.id
    route {
        cidr_block = var.route_table_cidr_block
        gateway_id = aws_internet_gateway.my-gateway.id
    }
    tags = var.aws_route_table
}

resource "aws_route_table_association" "my-route-table-association" {
    subnet_id = aws_subnet.this.id
    route_table_id = aws_route_table.my-route-table.id
}

# resource "aws_security_group" "this" {
#     name = "my-sec-group"
#     description = "Allow SSH and HTTP traffic"
#     vpc_id = aws_vpc.this.id


#     egress {
#         from_port = var.egress_from_port
#         to_port = var.egress_to_port
#         protocol = var.egress_protocol
#         cidr_blocks = var.egress_cidr_block
#     }

#     ingress {
#         from_port = var.ingress_from_port
#         to_port = var.ingress_to_port
#         protocol = var.ingress_protocol
#         cidr_blocks = var.cidr_block
#     }

#     tags = {
#         Name = var.security_group_name
#     }
# }