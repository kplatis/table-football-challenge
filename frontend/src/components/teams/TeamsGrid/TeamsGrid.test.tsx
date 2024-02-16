import '@testing-library/jest-dom'
import { render, screen } from '@testing-library/react'
import TeamsGrid from '../TeamsGrid'
import Providers from '@/components/Providers'
import { mockTeams } from '@/__tests__/mockData/teams'

// Mock useTeams hook
jest.mock('@/hooks/useTeams')

jest.mock('next/navigation', () => ({
  useRouter() {
    return {
      prefetch: () => null,
    }
  },
}))

describe('TeamsGrid', () => {
  test('renders loader when teams are loading', () => {
    jest
      .spyOn(require('@/hooks/useTeams'), 'default')
      .mockImplementation(() => ({
        isLoading: true,
        data: mockTeams,
      }))
    render(
      <Providers>
        <TeamsGrid />
      </Providers>,
    )

    // Check if loader is rendered
    expect(screen.getByTestId('loader')).toBeInTheDocument()
  })

  test('renders teams grid when teams are loaded', () => {
    jest
      .spyOn(require('@/hooks/useTeams'), 'default')
      .mockImplementation(() => ({
        isLoading: false,
        data: mockTeams,
      }))
    render(
      <Providers>
        <TeamsGrid />
      </Providers>,
    )

    // Check if team cards are rendered
    expect(screen.getByText('team1')).toBeInTheDocument()
    expect(screen.getByText('team2')).toBeInTheDocument()
  })

  test('renders error message when teams failed to load', () => {
    jest
      .spyOn(require('@/hooks/useTeams'), 'default')
      .mockImplementation(() => ({
        isLoading: false,
        data: null,
      }))
    render(
      <Providers>
        <TeamsGrid />
      </Providers>,
    )

    // Check if error message is rendered
    expect(screen.getByText('Something went wrong')).toBeInTheDocument()
  })
})
