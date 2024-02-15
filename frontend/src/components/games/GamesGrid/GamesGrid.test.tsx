import '@testing-library/jest-dom'
import { render, screen } from '@testing-library/react'
import GamesGrid from '.'
import { MantineProvider } from '@mantine/core'
import { mockGames } from '@/__tests__/mockData/games'
import { QueryClient, QueryClientProvider } from 'react-query'

const queryClient = new QueryClient()

describe('GamesGrid component', () => {
  test('renders loader when data is loading', () => {
    jest
      .spyOn(require('@/hooks/useGames'), 'default')
      .mockImplementation(() => ({
        isLoading: true,
        data: null,
      }))

    render(
      <MantineProvider defaultColorScheme="dark">
        <GamesGrid />
      </MantineProvider>,
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
      <QueryClientProvider client={queryClient}>
        <MantineProvider defaultColorScheme="dark">
          <GamesGrid />
        </MantineProvider>
      </QueryClientProvider>,
    )

    expect(screen.getAllByTestId('game-card')).toHaveLength(mockGames.length)
  })

  //   test('renders null when data is not available', () => {

  //     // Render the GamesGrid component
  //     render(
  //       <MantineProvider defaultColorScheme="dark">
  //         <GamesGrid />
  //       </MantineProvider>,
  //     )

  //     // Expect null to be returned
  //     expect(screen.queryByTestId('loader')).toBeNull()
  //     expect(screen.queryByTestId('game-card')).toBeNull()
  //   })
})
