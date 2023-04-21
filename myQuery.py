class MyQuery:
    @staticmethod
    def my_request(operation, company_name=None, buy_power=None):
        if operation == "current_price" and company_name is None:
            raise ValueError("Company name is required for current price query")

        if operation == "buy_power" and buy_power is None:
            raise ValueError("Buy power is required for buy power query")

        match operation:
            case "current_price":
                # perform query using company_name and buy_power
                return  # result of query
            case "buy_power":
                if company_name is not None:
                    # perform query using company_name and buy_power
                    return  # result of query
                else:
                    # perform query using buy_power only
                    return  # result of query
            case _:
                raise ValueError("Invalid operation")
