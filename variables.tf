variable "AWS_REGION" {
  type = string
  default = "us-east-1"
}

variable "vpc_cidr" {
  type = string
}

variable "subnet_cidr" {
  type = string
}

variable "subnet_tags" {
  type = map(string)
}

variable "vpc_tags" {
  type = map(string)
}

variable "gateway_tags" {
  type = map(string)
}

variable "aws_route_table" {
  type = map(string)
}
  
variable "ingress_from_port" {
  type = number
  
}

variable "ingress_to_port" {
  type = number
}

variable "ingress_protocol" {
  type = string
}

variable "egress_from_port" {
  type = number
}

variable "egress_to_port" {
  type = number
}

variable "egress_cidr_block" {
    type = list(string)
}
  
variable security_group_name {
  type = string
}

variable "AMI" {
  type = string
  default = "ami-0b0dcb5067f052a63"
}
  
variable "instances" {
    type = list(object({
      size = string
      name = string
      security_group = string
      }))
  }

variable "availability_zone" {
    type = string
}

variable "egress_protocol" {
    type = number
}

variable "cidr_block" {
    type = list(string)
}

variable "route_table_cidr_block" {
    type = string
}

variable "route_table_gateway_id" {
    type = string
}
  
variable "route_table_tags" {
    type = map(string)
}

variable "user" {
  type = list(string)
}
