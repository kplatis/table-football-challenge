'use client'

import { MantineProvider } from '@mantine/core'
import { QueryClient, QueryClientProvider } from 'react-query'

export default function Providers({ children }: { children: React.ReactNode }) {
  const queryClient = new QueryClient()

  return (
    <QueryClientProvider client={queryClient}>
      <MantineProvider defaultColorScheme="dark">{children}</MantineProvider>
    </QueryClientProvider>
  )
}
