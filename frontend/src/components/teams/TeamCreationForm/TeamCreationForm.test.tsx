import '@testing-library/jest-dom'
import { render, screen } from '@testing-library/react'
import TeamCreationForm from '../TeamCreationForm'
import { mockPlayers } from '@/__tests__/mockData/players'
import Providers from '@/components/Providers'

// Mock usePlayers hook
jest.mock('@/hooks/usePlayers')
jest.mock('axios')

describe('TeamCreationForm', () => {
  test('renders loader when players are loading', () => {
    // Mock isLoading as true
    jest
      .spyOn(require('@/hooks/usePlayers'), 'default')
      .mockImplementation(() => ({
        isLoading: true,
        data: mockPlayers,
      }))
    render(
      <Providers>
        <TeamCreationForm />
      </Providers>,
    )

    // Check if loader is rendered
    expect(screen.getByTestId('loader')).toBeInTheDocument()
  })

  test('renders team creation form when players are loaded', async () => {
    jest
      .spyOn(require('@/hooks/usePlayers'), 'default')
      .mockImplementation(() => ({
        isLoading: false,
        data: mockPlayers,
      }))
    render(
      <Providers>
        <TeamCreationForm />
      </Providers>,
    )

    // Check if team creation form is rendered
    expect(screen.getByTestId('name-input')).toBeInTheDocument()
    expect(screen.getByTestId('first-player-select')).toBeInTheDocument()
    expect(screen.getByTestId('second-player-select')).toBeInTheDocument()
    expect(screen.getByTestId('create-new-player-button')).toBeInTheDocument()
    expect(screen.getByTestId('create-new-team-button')).toBeInTheDocument()
  })
})
