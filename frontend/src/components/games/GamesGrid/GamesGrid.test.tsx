import '@testing-library/jest-dom'
import { render, screen } from '@testing-library/react'
import GamesGrid from '.'
import { mockGames } from '@/__tests__/mockData/games'
import Providers from '@/components/Providers'

describe('GamesGrid component', () => {
  test('renders loader when data is loading', () => {
    jest
      .spyOn(require('@/hooks/useGames'), 'default')
      .mockImplementation(() => ({
        isLoading: true,
        data: null,
      }))

    render(
      <Providers>
        <GamesGrid />
      </Providers>,
    )

    // Expect loader to be rendered
    expect(screen.getByTestId('loader')).toBeInTheDocument()
  })

  test('renders game cards when data is loaded', () => {
    jest
      .spyOn(require('@/hooks/useGames'), 'default')
      .mockImplementation(() => ({
        isLoading: false,
        data: mockGames,
      }))

    render(
      <Providers>
        <GamesGrid />
      </Providers>,
    )

    expect(screen.getAllByTestId('game-card')).toHaveLength(mockGames.length)
  })

  test('renders null when data is not available', () => {
    jest
      .spyOn(require('@/hooks/useGames'), 'default')
      .mockImplementation(() => ({
        isLoading: false,
        data: null,
      }))

    // Render the GamesGrid component
    render(
      <Providers>
        <GamesGrid />
      </Providers>,
    )

    // Expect null to be returned
    expect(screen.queryByTestId('loader')).toBeNull()
    expect(screen.queryByTestId('game-card')).toBeNull()
  })
})
