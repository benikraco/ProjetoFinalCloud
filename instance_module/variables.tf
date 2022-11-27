variable "name" {
    type = string
}

variable "type" {
  type = string
}

variable "ingress_from_port" {
  type = number
  default = 22
}

variable "ingress_to_port" {
  type = number
  default = 22
}

variable "ingress_protocol" {
  type = string
  default = "tcp"
}

variable "egress_from_port" {
  type = number
  default = 0
}

variable "egress_to_port" {
  type = number
  default = 0
}

variable "egress_cidr_block" {
    type = list(string)
    default = ["0.0.0.0/0"]
}

variable "cidr_block" {
    type = list(string)
    default = ["0.0.0.0/0"]
}

# variable "aws_subnet" {
#     type = string
# }

# variable "vpc_id" {
#     type = string
# }

# variable "security_group_name" {
#   type = string
# }

variable "AMI" {
    type = string
    default = "ami-0b0dcb5067f052a63"
}

variable "vpc_id" {
    type = string
}

variable "subnet_id" {
    type = string
}

variable "egress_protocol" {
    type = string
    default = "tcp"
}

variable "security_group" {
    type = string
}

variable "availability_zone" {
    type = string
}

# variable "route_table_id" {
#     type = string
# }

variable "route_table_cidr_block" {
    type = string
}

variable "route_table_gateway_id" {
    type = string
}

variable "route_table_tags" {    
    type = map(string) 
}

variable "AWS_REGION" {
    type = string
    default = "us-east-1"
}
  
# variable "instance_type" { 
#     type = string
# }