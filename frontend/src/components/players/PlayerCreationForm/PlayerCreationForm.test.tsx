import '@testing-library/jest-dom'
import { render, screen, fireEvent, waitFor } from '@testing-library/react'
import axios from 'axios'
import PlayerCreationForm from '../PlayerCreationForm'
import Providers from '@/components/Providers'

// Mock axios post
jest.mock('axios')

describe('PlayerCreationForm', () => {
  afterEach(() => {
    jest.clearAllMocks()
  })
  test('submits form data when submitted', async () => {
    render(
      <Providers>
        <PlayerCreationForm onSuccessFn={() => {}} />
      </Providers>,
    )

    jest.mock('axios')
    const mAxiosPost = jest.mocked(axios.post)
    // Mock successful response from axios post
    mAxiosPost.mockResolvedValueOnce({ status: 200 })

    // Fill out the form
    fireEvent.change(screen.getByTestId('name-input'), {
      target: { value: 'John Doe' },
    })

    // Submit the form
    fireEvent.click(screen.getByTestId('create-player-button'))

    // Wait for the axios post call to be resolved
    await waitFor(() => expect(axios.post).toHaveBeenCalledTimes(1))

    // Check if the success notification is shown
    expect(
      screen.getByText('Success! Your player has been created.'),
    ).toBeInTheDocument()
  })

  test('calls onSuccessFn when player is successfully created', async () => {
    const onSuccessFn = jest.fn()
    render(
      <Providers>
        <PlayerCreationForm onSuccessFn={onSuccessFn} />
      </Providers>,
    )

    jest.mock('axios')
    const mAxiosPost = jest.mocked(axios.post)
    // Mock successful response from axios post
    mAxiosPost.mockResolvedValueOnce({ status: 200 })

    // Fill out the form
    fireEvent.change(screen.getByTestId('name-input'), {
      target: { value: 'John Doe' },
    })

    // Submit the form
    fireEvent.click(screen.getByTestId('create-player-button'))

    // Wait for the axios post call to be resolved
    await waitFor(() => expect(mAxiosPost).toHaveBeenCalledTimes(1))

    // Check if onSuccessFn is called
    expect(onSuccessFn).toHaveBeenCalledTimes(1)
  })

  test('does not submit form data if validation fails', async () => {
    render(
      <Providers>
        <PlayerCreationForm onSuccessFn={() => {}} />
      </Providers>,
    )

    // Fill out the form with invalid data (less than 2 characters)
    fireEvent.change(screen.getByTestId('name-input'), {
      target: { value: 'J' },
    })

    // Submit the form
    fireEvent.click(screen.getByTestId('create-player-button'))

    // Wait for a short delay to ensure no axios calls are made
    await waitFor(() => expect(axios.post).not.toHaveBeenCalled())

    // Check if error message is shown
    expect(
      screen.getByText('Name must be at least 2 characters long.'),
    ).toBeInTheDocument()
  })
})
