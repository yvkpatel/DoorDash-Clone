import { render, screen, cleanup, fireEvent } from "@testing-library/react";
import renderer from "react-test-renderer";
import userEvent from "@testing-library/user-event";
import React, { useEffect } from "react";
import { BrowserRouter } from "react-router-dom";
import ReactDOM from "react-dom";
import Button from "../../Button";

import PaymentPage from "../payment/PaymentPage";
import OrderSummary from "../payment/OrderSummary";
import Payment from "../payment/Payment";
import "@testing-library/jest-dom/extend-expect";

afterEach(() => {
  cleanup();
});

const MockOrderSummary = {
  location: {
    state: {
      cart: {
        itemList: [
          {
            id: 1,
            title: "Fries",
            price: 3.55,
          },
        ],
      },
    },
  },
};

test("should render customer payment component", () => {
  render(
    <BrowserRouter>
      <PaymentPage {...MockOrderSummary} />
    </BrowserRouter>
  );
  const PaymentPageElement = screen.getByTestId("payment-page");
  expect(PaymentPageElement).toBeDefined();
});

test("should should show order summary", () => {
  const { getByText } = render(
    <OrderSummary
      itemList={MockOrderSummary.location.state.cart.itemList}
      price="3.55"
    />
  );

  expect(getByText("Fries")).toBeTruthy();
});

test("should should show payment information field", () => {
  const { getByText } = render(<Payment />);

  expect(getByText("Payment Information")).toBeTruthy();
});

test("matches snapshot", () => {
  const tree = renderer.create(
    <BrowserRouter>
      <PaymentPage {...MockOrderSummary} />
    </BrowserRouter>
  );
  expect(tree).toMatchSnapshot();
});
